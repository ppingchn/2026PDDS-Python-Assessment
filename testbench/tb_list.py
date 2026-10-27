import contextlib
import io
import runpy
import unittest
from pathlib import Path


SUBMISSION_DIR = Path(__file__).resolve().parents[1] / "python_list_src"


def find_submission():
	"""Find the single Python file submitted in the list exercise directory."""
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


class PythonListExerciseTest(unittest.TestCase):
	DESCRIPTIONS = {
		"test_section_1_user_orders": "Section 1: List Joining (user_orders)",
		"test_section_2_grouped": "Section 2: List Grouping (grouped)",
		"test_section_3_sorted_grouped": "Section 3: List Sorting (sorted_grouped)",
		"test_section_4_highest_total_price_user": "Section 4: List Indexing (highest_total_price_user)",
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

	def test_section_1_user_orders(self):
		user_orders = self.require_variable("user_orders")
		expected = [
			{"id": 1, "name": "Alice", "user_id": 1, "price": 1000},
			{"id": 2, "name": "Bob", "user_id": 2, "price": 500},
			{"id": 3, "name": "Alice", "user_id": 1, "price": 200},
		]
		self.assertEqual(user_orders, expected)

	def test_section_2_grouped(self):
		grouped = self.require_variable("grouped")
		expected = {
			"Alice": {"total_price": 1200, "order_count": 2},
			"Bob": {"total_price": 500, "order_count": 1},
		}
		self.assertEqual(grouped, expected)

	def test_section_3_sorted_grouped(self):
		sorted_grouped = self.require_variable("sorted_grouped")
		expected = [
			("Alice", {"total_price": 1200, "order_count": 2}),
			("Bob", {"total_price": 500, "order_count": 1}),
		]
		self.assertEqual(sorted_grouped, expected)

	def test_section_4_highest_total_price_user(self):
		highest_total_price_user = self.require_variable("highest_total_price_user")
		expected = {"name": "Alice", "total_price": 1200, "order_count": 2}
		self.assertEqual(highest_total_price_user, expected)


if __name__ == "__main__":
	unittest.main(testRunner=DescriptiveTestRunner, verbosity=2)
