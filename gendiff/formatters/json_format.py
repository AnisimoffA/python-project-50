from gendiff.interface import local_formater, json_format_dict
import itertools


item = [['-', 'group2', [['', 'abc', 12345], ['', 'deep', [['', 'id', 45]]]]], ['+', 'group3', [['', 'fee', 100500], ['', 'deep', [['', 'id', [['', 'number', 45]]]]]]], ['', 'common', [['', 'setting1', 'Value 1'], ['-', 'setting2', 200], ['+', 'setting5', [['', 'key5', 'value5']]], ['+', 'follow', False], ['+', 'setting4', 'blah blah'], ['change-', 'setting3', True], ['change+', 'setting3', [['', 'key', 'value']]], ['', 'setting6', [['', 'key', 'value'], ['+', 'ops', 'vops'], ['', 'doge', [['change-', 'wow', 'too much'], ['change+', 'wow', 'so much']]]]]]], ['', 'group1', [['', 'foo', 'bar'], ['change-', 'nest', [['', 'key', 'value']]], ['change+', 'nest', 'str'], ['change-', 'baz', 'bas'], ['change+', 'baz', 'bars']]], ['', 'group4', [['+', 'key', False], ['+', 'someKey', True], ['change-', 'type', 'bas'], ['change+', 'type', 'bar'], ['change-', 'foo', 0], ['change+', 'foo', None], ['change-', 'default', None], ['change+', 'default', ''], ['change-', 'isNested', False], ['change+', 'isNested', 'none'], ['', 'nest', [['-', 'isNested', True], ['change-', 'bar', ''], ['change+', 'bar', 0]]]]]]

def json_format(value, replacer=' ', spaces_count=4):  # noqa
    value = json_format_dict(value)

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return local_formater(current_value, "json_format")

        deep_size = depth + spaces_count
        deep_indent = replacer * deep_size
        current_indent = replacer * depth
        lines = []
        
        count = 0
        need = len(current_value)
        for k, meta in current_value.items():
            count += 1
            if k == "mark":
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"mark": "{meta}"{comma}')
                continue
            elif k == "value":
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"value": {iter_(meta, deep_size)}{comma}')
                continue

            if meta["mark"] != "+" and meta["mark"] != "-":
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"{k}": {iter_(meta, deep_size)}{comma}')
            else:
                comma = comma_check(count, need)
                lines.append(f'{deep_indent}"{k}": {iter_(meta, deep_size)}{comma}')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)

def comma_check(counter, predict):
    if counter == predict:
        return ""
    return ","
