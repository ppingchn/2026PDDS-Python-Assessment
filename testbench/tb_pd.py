import contextlib
import io
import runpy
import unittest
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal


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


class PandasExerciseTest(unittest.TestCase):
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
		return self.namespace[name]

	def test_users_dataframe(self):
		users_df = self.require_variable("users_df")
		expected = pd.DataFrame(
			[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
		)
		assert_frame_equal(users_df.reset_index(drop=True), expected)

	def test_orders_dataframe(self):
		orders_df = self.require_variable("orders_df")
		expected = pd.DataFrame(
			[
				{"id": 1, "user_id": 1, "price": 1000},
				{"id": 2, "user_id": 2, "price": 500},
				{"id": 3, "user_id": 1, "price": 200},
			]
		)
		assert_frame_equal(orders_df.reset_index(drop=True), expected)

	def test_merged_dataframe(self):
		merged_df = self.require_variable("merged_df")
		expected = pd.DataFrame(
			[
				{"id_x": 1, "name": "Alice", "id_y": 1, "user_id": 1, "price": 1000},
				{"id_x": 1, "name": "Alice", "id_y": 3, "user_id": 1, "price": 200},
				{"id_x": 2, "name": "Bob", "id_y": 2, "user_id": 2, "price": 500},
			]
		)
		assert_frame_equal(merged_df.reset_index(drop=True), expected)

	def test_grouped_and_sorted_dataframe(self):
		grouped_sorted_df = self.require_variable("grouped_sorted_df")
		expected = pd.DataFrame(
			[
				{"name": "Alice", "total_price": 1200, "order_count": 2},
				{"name": "Bob", "total_price": 500, "order_count": 1},
			]
		)
		actual = grouped_sorted_df.reset_index(drop=True)
		if "name" not in actual.columns and actual.index.name == "name":
			actual = actual.reset_index()
		assert_frame_equal(actual.reset_index(drop=True), expected)

	def test_top_user(self):
		top_user = self.require_variable("top_user")
		self.assertIsInstance(top_user, pd.Series)

		if "name" in top_user.index:
			self.assertEqual(top_user["name"], "Alice")
		else:
			self.assertEqual(top_user.name, "Alice")
		self.assertEqual(top_user["total_price"], 1200)
		self.assertEqual(top_user["order_count"], 2)


if __name__ == "__main__":
	unittest.main()
