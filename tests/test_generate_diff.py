from gendiff.generate_diff import generate_diff

def test_generate_diff():
    assert generate_diff('gendiff/test/fixtures/file1.json', 'gendiff/test/fixtures/file2.json') == 