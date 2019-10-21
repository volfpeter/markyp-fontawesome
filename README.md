[![Build Status](https://travis-ci.org/volfpeter/markyp-fontawesome.svg?branch=master)](https://travis-ci.org/volfpeter/markyp-fontawesome)
[![Downloads](https://pepy.tech/badge/markyp-fontawesome)](https://pepy.tech/project/markyp-fontawesome)
[![Downloads](https://pepy.tech/badge/markyp-fontawesome/month)](https://pepy.tech/project/markyp-fontawesome/month)
[![Downloads](https://pepy.tech/badge/markyp-fontawesome/week)](https://pepy.tech/project/markyp-fontawesome/week)

# markyp-fontawesome

Font Awesome 5 icons for web pages built with [markyp-html](https://github.com/volfpeter/markyp-html).

## Installation

The project is listed on the Python Package Index, it can be installed simply by executing `pip install markyp-fontawesome`.

## Getting started

### Font Awesome setup

First of all, you should acquire a Font Awesome kit code [here](https://fontawesome.com/start).

### Creating icons for `markyp-html` web pages

If you are not familiar with the basic concepts of `markyp`, please start by having a look at its documentation [here](https://github.com/volfpeter/markyp).

The following example code shows the creation of a web page that displays a large, spinning Python logo over a solid square.

```Python
# markyp-html web page element
from markyp_html import webpage

# Font Awesome imports
from markyp_fontawesome import kit_import, brand, solid, stack, IconStyle as IS

# Your Font Awesome kit code
fa_kit_code = "a076d05399"

page = webpage(
    # 3x-sized Font Awesome icon stack
    stack.x3(
        # Solid square icon for the background
        solid("square", class_=IS.stacked_size_2x),
        # Inverse Python brand icon for the foreground
        brand("python", class_=f"{IS.stacked_size_2x} {IS.inverse} {IS.spin}"),
    ),
    page_title="markyp-fontawesome demo",
    # Font Awesome kit import with kit code
    javascript=[kit_import(fa_kit_code)],
)

print(page)
```

Things to note from the example:

- You need to pass the Font Awesome import element to the `javascript` keyword argument of `webpage()` to be able to display Font Awesome icons on the page.
- `stack()` and its factory methods like `x3()` let you create Font Awesome icon stacks.
- `brand` and `solid` (and their factory methods) let you create Font Awesome icons of Brands and Solid styles. (Pro styles are also supported.)
- The `IconStyle` enumeration class lets you customize icons by passing its properties to the icons' `class_` argument.

For more details on how this package works, please see [markyp](https://github.com/volfpeter/markyp) and [markyp-html](https://github.com/volfpeter/markyp-html).

For more details on how to use Font Awesome 5, see [this](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use) page.

## Community guidelines

In general, please treat each other with respect and follow the below guidelines to interact with the project:

- _Questions, feedback_: Open an issue with a `[Question] <issue-title>` title.
- _Bug reports_: Open an issue with a `[Bug] <issue-title>` title, an adequate description of the bug, and a code snippet that reproduces the issue if possible.
- _Feature requests and ideas_: Open an issue with an `[Enhancement] <issue-title>` title and a clear description of the enhancement proposal.

## Contribution guidelines

Every form of contribution is welcome, including documentation improvements, tests, bug fixes, and feature implementations.

Please follow these guidelines to contribute to the project:

- Make sure your changes match the documentation and coding style of the project, including [PEP 484](https://www.python.org/dev/peps/pep-0484/) type annotations.
- `mypy` is used to type-check the codebase, submitted code should not produce typing errors. See [this page](http://mypy-lang.org/) for more information on `mypy`.
- _Small_ fixes can be submitted simply by creating a pull request.
- Non-trivial changes should have an associated [issue](#community-guidelines) in the issue tracker that commits must reference (typically by adding `#refs <issue-id>` to the end of commit messages).
- Please write [tests](#testing) for the changes you make (if applicable).

If you have any questions about contributing to the project, please contact the project owner.

As mentioned in the [contribution guidelines](#contribution-guidelines), the project is type-checked using `mypy`, so first of all, the project must pass `mypy`'s static code analysis.

The project is tested using `pytest`. The chosen test layout is that tests are outside the application code, see [this page](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code) for details on what it means in practice.

If `pytest` is installed, the test set can be executed using the `pytest test` command from within the project directory.

If `pytest-cov` is also installed, a test coverage report can be generated by executing `pytest test --cov markyp_fontawesome` from the root directory of the project.

## License - MIT

The library is open-sourced under the conditions of the MIT [license](https://choosealicense.com/licenses/mit/).

