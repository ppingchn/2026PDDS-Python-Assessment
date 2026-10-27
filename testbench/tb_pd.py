import contextlib
import io
import runpy
import unittest
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal


SUBMISSION_DIR = Path(__file__).resolve().parents[1] / "pandas_src"


def find_submission():
	"""Find the single Python file submitted in the pandas exercise directory."""
	candidates = sorted(
		path for path in SUBMISSION_DIR.glob("*.py") if not path.name.startswith("__")
	)
	if len(candidates) != 1:
		names = ", ".join(path.name for path in candidates) or "none"
		raise RuntimeError(
			f"Expected exactly one Python submission in {SUBMISSION_DIR}; "
			f"found {len(candidates)} ({names})"
		)
	return candidates[0]


class DescriptiveTestResult(unittest.TextTestResult):
	def addSuccess(self, test):
		unittest.TestResult.addSuccess(self, test)
		if self.showAll:
			self.stream.writeln("PASS")
		elif self.dots:
			self.stream.write(".")
			self.stream.flush()


class DescriptiveTestRunner(unittest.TextTestRunner):
	resultclass = DescriptiveTestResult


class PandasExerciseTest(unittest.TestCase):
	DESCRIPTIONS = {
		"test_section_1_1_users_dataframe": "Section 1: DataFrame Creation (users_df)",
		"test_section_1_2_orders_dataframe": "Section 1: DataFrame Creation (orders_df)",
		"test_section_2_merged_dataframe": "Section 2: DataFrame Merging (merged_df)",
		"test_section_3_grouped_and_sorted_dataframe": "Section 3: DataFrame Grouping & Sorting (grouped_sorted_df)",
		"test_section_4_highest_total_price_user": "Section 4: DataFrame Indexing (highest_total_price_user)",
	}

	def shortDescription(self):
		return None

	def __str__(self):
		return self.DESCRIPTIONS.get(self._testMethodName, super().__str__())

	@classmethod
	def setUpClass(cls):
		cls.submission_path = None
		cls.namespace = None
		cls.execution_error = None

		try:
			cls.submission_path = find_submission()
			with contextlib.redirect_stdout(io.StringIO()):
				cls.namespace = runpy.run_path(str(cls.submission_path))
		except Exception as error:  # Report the student's script error in each test.
			cls.execution_error = error

	def require_successful_execution(self):
		self.assertIsNone(
			self.execution_error,
			f"Student submission could not be executed: {self.execution_error}",
		)

	def require_variable(self, name):
		self.require_successful_execution()
		if self.namespace is None:
			self.fail("The student script did not produce a namespace")
		self.assertIn(name, self.namespace, f"Missing required variable: {name}")
		value = self.namespace[name]
		self.assertIsNotNone(
			value,
			f"Variable '{name}' is still None — replace the placeholder with your solution.",
		)
		return value

	def test_section_1_1_users_dataframe(self):
		users_df = self.require_variable("users_df")
		expected = pd.DataFrame(
			[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
		)
		assert_frame_equal(users_df.reset_index(drop=True), expected)

	def test_section_1_2_orders_dataframe(self):
		orders_df = self.require_variable("orders_df")
		expected = pd.DataFrame(
			[
				{"id": 1, "user_id": 1, "price": 1000},
				{"id": 2, "user_id": 2, "price": 500},
				{"id": 3, "user_id": 1, "price": 200},
			]
		)
		assert_frame_equal(orders_df.reset_index(drop=True), expected)

	def test_section_2_merged_dataframe(self):
		"""
		Accept any merge order that produces the correct logical content:
		one row per order, with the matching user's name attached. Row order
		is normalised by order id (id_y) before comparison.
		"""
		merged_df = self.require_variable("merged_df")

		# Determine which column holds the order id.
		order_id_col = "id_y" if "id_y" in merged_df.columns else "id"

		# Normalise: sort by order id and reset index for a clean comparison.
		actual = merged_df.sort_values(order_id_col).reset_index(drop=True)

		expected = pd.DataFrame(
			[
				{"id_x": 1, "name": "Alice", "id_y": 1, "user_id": 1, "price": 1000},
				{"id_x": 1, "name": "Alice", "id_y": 3, "user_id": 1, "price": 200},
				{"id_x": 2, "name": "Bob",   "id_y": 2, "user_id": 2, "price": 500},
			]
		).sort_values("id_y").reset_index(drop=True)

		# If the student merged in the opposite order (orders LEFT JOIN users),
		# the id columns will be swapped. Accept both orientations.
		if set(actual.columns) != set(expected.columns):
			# Try renaming id_x <-> id_y if that fixes the column set.
			rename_map = {}
			if "id_x" in actual.columns and "id_y" not in actual.columns:
				rename_map = {"id_x": "id_y", "id": "id_x"}
			elif "id_y" in actual.columns and "id_x" not in actual.columns:
				rename_map = {"id_y": "id_x", "id": "id_y"}
			if rename_map:
				actual = actual.rename(columns=rename_map)

		assert_frame_equal(
			actual[expected.columns],
			expected,
			check_like=True,  # column order doesn't matter
		)

	def test_section_3_grouped_and_sorted_dataframe(self):
		"""
		Verify that grouped_sorted_df contains the correct totals *and* that
		each total is associated with the correct user name.

		Accepts 'name' as either the index or a regular column.
		"""
		grouped_sorted_df = self.require_variable("grouped_sorted_df")

		# Normalise: bring 'name' into a regular column for easy comparison.
		df = grouped_sorted_df.copy()
		if df.index.name == "name":
			df = df.reset_index()  # name becomes a regular column
		elif "name" not in df.columns:
			self.fail(
				"grouped_sorted_df must have 'name' as either the index or a column."
			)

		# Required columns must be present.
		for col in ("name", "total_price", "order_count"):
			self.assertIn(
				col, df.columns,
				f"grouped_sorted_df is missing the required column '{col}'.",
			)

		# Build the expected frame sorted by total_price descending.
		expected = pd.DataFrame(
			[
				{"name": "Alice", "total_price": 1200, "order_count": 2},
				{"name": "Bob",   "total_price": 500,  "order_count": 1},
			]
		)

		# Sort and reset both for a clean row-by-row comparison.
		actual_sorted = (
			df[["name", "total_price", "order_count"]]
			.sort_values("total_price", ascending=False)
			.reset_index(drop=True)
		)

		assert_frame_equal(actual_sorted, expected, check_like=False)

	def test_section_4_highest_total_price_user(self):
		# Accept highest_total_price_user (preferred) or top_user for backwards compatibility.
		target_var = "highest_total_price_user"
		if self.namespace is not None and target_var not in self.namespace and "top_user" in self.namespace:
			target_var = "top_user"

		highest_total_price_user = self.require_variable(target_var)
		self.assertIsInstance(highest_total_price_user, pd.Series)

		# Accept 'name' stored either as the Series.name or as an index label.
		if "name" in highest_total_price_user.index:
			self.assertEqual(highest_total_price_user["name"], "Alice",
				f"{target_var} should belong to 'Alice'")
		else:
			self.assertEqual(highest_total_price_user.name, "Alice",
				f"{target_var}.name should be 'Alice'")

		self.assertEqual(highest_total_price_user["total_price"], 1200)
		self.assertEqual(highest_total_price_user["order_count"], 2)


if __name__ == "__main__":
	unittest.main(testRunner=DescriptiveTestRunner, verbosity=2)
