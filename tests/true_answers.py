TRUE_FLATTEN = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

TRUE_NONFLATTEN = '''{
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

TRUE_FLATTEN_PLAIN = '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''

TRUE_NONFLATTEN_PLAIN = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

TRUE_NONFLATTEN_JSON_FORMAT = '''{
    "common": {
        "mark": "",
        "value": {
            "follow": {
                "mark": "+",
                "value": false,
            },
            "setting1": {
                "mark": "",
                "value": "Value 1",
            },
            "setting2": {
                "mark": "-",
                "value": 200,
            },
            "setting3": {
                "mark": "+",
                "value": null,
            },
            "setting4": {
                "mark": "+",
                "value": "blah blah",
            },
            "setting5": {
                "mark": "+",
                "value": {
                    "key5": {
                        "mark": "",
                        "value": "value5",
                    },
                },
            },
            "setting6": {
                "mark": "",
                "value": {
                    "doge": {
                        "mark": "",
                        "value": {
                            "wow": {
                                "mark": "+",
                                "value": "so much",
                            },
                        },
                    },
                    "key": {
                        "mark": "",
                        "value": "value",
                    },
                    "ops": {
                        "mark": "+",
                        "value": "vops",
                    },
                },
            },
        },
    },
    "group1": {
        "mark": "",
        "value": {
            "baz": {
                "mark": "+",
                "value": "bars",
            },
            "foo": {
                "mark": "",
                "value": "bar",
            },
            "nest": {
                "mark": "+",
                "value": "str",
            },
        },
    },
    "group2": {
        "mark": "-",
        "value": {
            "abc": {
                "mark": "",
                "value": 12345,
            },
            "deep": {
                "mark": "",
                "value": {
                    "id": {
                        "mark": "",
                        "value": 45,
                    },
                },
            },
        },
    },
    "group3": {
        "mark": "+",
        "value": {
            "deep": {
                "mark": "",
                "value": {
                    "id": {
                        "mark": "",
                        "value": {
                            "number": {
                                "mark": "",
                                "value": 45,
                            },
                        },
                    },
                },
            },
            "fee": {
                "mark": "",
                "value": 100500,
            },
        },
    },
}'''

TRUE_FLATTEN_JSON_FORMAT = '''{
    "follow": {
        "mark": "-",
        "value": false,
    },
    "host": {
        "mark": "",
        "value": "hexlet.io",
    },
    "proxy": {
        "mark": "-",
        "value": "123.234.53.22",
    },
    "timeout": {
        "mark": "+",
        "value": 20,
    },
    "verbose": {
        "mark": "+",
        "value": true,
    },
}'''