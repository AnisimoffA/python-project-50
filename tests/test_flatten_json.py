from gendiff import diff_gen

def test_json():
    answer = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert diff_gen.generate_diff("file1.json","file2.json") == answer

