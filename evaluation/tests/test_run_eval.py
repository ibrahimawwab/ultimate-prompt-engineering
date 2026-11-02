import json
import unittest
from pathlib import Path
from evaluation.run_eval import estimate_cost, load_cases, validate_config, validate_output

class EvaluationHarnessTests(unittest.TestCase):
    def test_valid_output(self):
        value = {'category':'billing','summary':'Duplicate charge reported.','missing_information':[],'rationale':'The ticket says charged twice.'}
        self.assertTrue(validate_output(json.dumps(value))['valid'])

    def test_markdown_fence_is_rejected(self):
        self.assertFalse(validate_output('```json\\n{}\\n```')['valid'])

    def test_wrong_keys_are_rejected(self):
        value = {'category':'billing','summary':'x','missing_information':[],'rationale':'x','extra':'no'}
        self.assertEqual(validate_output(json.dumps(value))['error'], 'incorrect_keys')

    def test_invalid_category_is_rejected(self):
        value = {'category':'other','summary':'x','missing_information':[],'rationale':'x'}
        self.assertEqual(validate_output(json.dumps(value))['error'], 'invalid_category')

    def test_cost_requires_usage_and_both_rates(self):
        model = {'input_cost_per_1m_tokens':1.0,'output_cost_per_1m_tokens':2.0}
        self.assertIsNone(estimate_cost(model, None, 100))
        self.assertEqual(estimate_cost(model, 1000, 1000), 0.003)

    def test_fixture_has_twelve_unique_cases(self):
        cases = load_cases(Path(__file__).parents[1] / 'cases.jsonl')
        self.assertEqual(len(cases), 12)
        self.assertEqual(len({case['id'] for case in cases}), 12)

    def test_config_requires_model_metadata(self):
        with self.assertRaises(ValueError):
            validate_config({'settings':{'temperature':0,'max_tokens':100},'models':[{'name':'incomplete'}]})

if __name__ == '__main__':
    unittest.main()
