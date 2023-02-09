from gendiff import diff_gen
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from true_answers import TRUE_NONFLATTEN, TRUE_NONFLATTEN_PLAIN


def test_flatten_jaml():
    needed_diff_stylish = diff_gen.generate_diff("nonflatten_before.jaml","nonflatten_after.jaml", stylish)  # noqa: E501
    needed_diff_plain = diff_gen.generate_diff("nonflatten_before.jaml","nonflatten_after.jaml", plain)
    assert needed_diff_stylish == TRUE_NONFLATTEN
    assert needed_diff_plain == TRUE_NONFLATTEN_PLAIN
    
print(diff_gen.generate_diff("nonflatten_before.jaml","nonflatten_after.jml"))

'''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
            }
            key: value
          + ops: vops
        }
    }
    group1: {
        foo: bar
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

'''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''