from get_country_codes import get_country_codes

test_cases = [
    {
        "input": "NZ$300, KR$1200, DK$5",
        "output": "NZ, KR, DK",
    },
    {
        "input": "US$40, AU$89, JP$200",
        "output": "US, AU, JP",
    },
    {
        "input": "AU$23, NG$900, MX$200, BG$790, ES$2",
        "output": "AU, NG, MX, BG, ES",
    },
    {
        "input": "CA$40",
        "output": "CA",
    },
]

def test_assignment():
    for test_case in test_cases:
        assignment_response = get_country_codes(test_case['input'])
        assert assignment_response == test_case[
            'output'], f"""
For
\nInput:    {test_case['input']}
\nExpected: {test_case['output']}
\nGot:      {assignment_response}\n"""
