"""
Font Awesome icons for `markyp-html`-based webpages.
"""

__author__ = "Peter Volf"
__copyright__ = "Copyright 2019, Peter Volf"
__email__ = "do.volfp@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/volfpeter/markyp-fontawesome"
__version__ = "0.1910.0"

from markyp_fontawesome.factories import IconFactory, StackFactory
from markyp_html import inline, script

__all__ = (
    "kit_import",
    "IconStyle",
    "brand",
    "duotone",
    "light",
    "regular",
    "solid",
    "stack",
)


def kit_import(code: str) -> script:
    """
    Creates a Font Awesome import `script` tag with the given `code`.

    The import statement should typically be added to the `head` element of the page.

    See https://fontawesome.com/start.
    """
    return script.ref(f"https://kit.fontawesome.com/{code}.js")


class IconSet:
    """
    Prefixes for Font Awesome icon sets.

    See https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use.
    """

    solid = "fas"
    brands = "fab"

    regular = "far"
    light = "fal"
    duotone = "fad"


class IconStyle:
    """
    Font Awesome CSS class names that can be applied on the icons.

    See https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use for details.
    """

    fixed_width = "fa-fw"

    flip_horizontal = "fa-flip-horizontal"
    flip_vertical = "fa-flip-vertical"
    flip_both = "fa-flip-both"

    rotate_90 = "fa-rotate-90"
    rotate_180 = "fa-rotate-180"
    rotate_270 = "fa-rotate-270"

    spin = "fa-spin"
    pulse = "fa-pulse"

    border = "fa-border"
    inverse = "fa-inverse"

    pull_right = "fa-pull-right"
    pull_left = "fa-pull-left"

    stacked_size_1x = "fa-stack-1x"
    stacked_size_2x = "fa-stack-2x"
    stacked_size_3x = "fa-stack-3x"
    stacked_size_4x = "fa-stack-4x"
    stacked_size_5x = "fa-stack-5x"
    stacked_size_6x = "fa-stack-6x"
    stacked_size_7x = "fa-stack-7x"
    stacked_size_8x = "fa-stack-8x"
    stacked_size_9x = "fa-stack-9x"
    stacked_size_10x = "fa-stack-10x"


brand = IconFactory(inline.span, IconSet.brands)
"""
Factory that produces `Brand` icons.

See https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use.
"""

duotone = IconFactory(inline.span, IconSet.duotone)
"""
Factory that produces `Duotone` icons.

See https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use.
"""

light = IconFactory(inline.span, IconSet.light)
"""
Factory that produces `Light` icons.

See https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use.
"""

regular = IconFactory(inline.span, IconSet.regular)
"""
Factory that produces `Regular` icons.

See https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use.
"""

solid = IconFactory(inline.span, IconSet.solid)
"""
Factory that produces `Solid` icons.

See https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use.
"""

stack = StackFactory(inline.span)
"""
Groups for stacking multiple icons on each-other.

See https://fontawesome.com/how-to-use/on-the-web/styling/stacking-icons.
"""
