from gendiff import diff_gen
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from true_answers import TRUE_NONFLATTEN, TRUE_NONFLATTEN_PLAIN


def test_flatten_jaml():
    needed_diff_stylish = diff_gen.generate_diff("nonflatten_before.jaml","nonflatten_after.jaml", stylish) # noqa: E501
    needed_diff_plain = diff_gen.generate_diff("nonflatten_before.jaml","nonflatten_after.jaml", plain)
    assert needed_diff_stylish == TRUE_NONFLATTEN
    assert needed_diff_plain == TRUE_NONFLATTEN_PLAIN
    
    
    
print(diff_gen.generate_diff("nonflatten_before.json","nonflatten_after.json", plain))