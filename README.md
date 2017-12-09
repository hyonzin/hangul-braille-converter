Hangul to Braille Converter
----
python project for the blind
* Hangul
* English
* Number
* Some special symbols
----

USAGE:
```Python
import hbcvt
hbcvt.h2b.text("꽃이 피었어!")
```
RESULT:<br>
* The first 3 numbers are the left side of 6-dot braille numbers, and other 3 numbers are the right side.

```python
[
    ['꽃', [
        ['ㄲ', [
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0]
        ]],
        ['ㅗ', [
            [1, 0, 1, 0, 0, 1]
        ]],
        ['ㅊ', [
            [0, 1, 1, 0, 0, 0]
        ]]
    ]],
    ['이', [
        ['ㅇ', [
            [1, 1, 0, 1, 1, 0]
        ]],
        ['ㅣ', [
            [1, 0, 1, 0, 1, 0]
        ]]
    ]],
    [' ', [
        [' ', [
            [0, 0, 0, 0, 0, 0]
        ]]
    ]],
    ['피', [
        ['ㅍ', [
            [1, 0, 0, 1, 1, 0]
        ]],
        ['ㅣ', [
            [1, 0, 1, 0, 1, 0]
        ]]
    ]],
    ['었', [
        ['ㅇ', [
            [1, 1, 0, 1, 1, 0]
        ]],
        ['ㅓ', [
            [0, 1, 1, 1, 0, 0]
        ]],
        ['ㅆ', [
            [0, 0, 1, 1, 0, 0]
        ]]
    ]],
    ['어', [
        ['ㅇ', [
            [1, 1, 0, 1, 1, 0]
        ]],
        ['ㅓ', [
            [0, 1, 1, 1, 0, 0]
        ]]
    ]],
    ['!', [
        ['!', [
            [0, 1, 1, 0, 1, 0]
        ]]
    ]]
]
```
