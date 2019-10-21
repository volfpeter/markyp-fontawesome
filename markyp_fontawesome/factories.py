"""
Font Awesome element factories.
"""

from typing import Optional, Type

from markyp import ElementType, IElement, PropertyValue
from markyp_html import join


__all__ = ("IconFactory", "StackFactory")


class IconFactory:
    """
    Font Awesome icon factory.

    Instances of the factory are callable, calling the instance results in default-sized icons.
    """

    def __init__(self, factory: Type[IElement], prefix: Optional[str]) -> None:
        """
        Initialization.

        Arguments:
            factory: The element to create icons from.
            prefix: The Font Awesome style prefix (one of the values from `StylePrefixes`),
                    or `None` if the prefix is not necessary, for example for icon stacks.
        """
        self._factory = factory
        self._prefix = prefix

    def __call__(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a default-sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self._factory(class_=join(self._prefix, f"fa-{name}", class_), **kwargs)

    def default(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a default-sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=class_, **kwargs)

    def xs(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a extra-small-sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-xs"), **kwargs)

    def sm(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a small-sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-sm"), **kwargs)

    def lg(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a large-sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-lg"), **kwargs)

    def x2(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 2x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-2x"), **kwargs)

    def x3(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 3x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-3x"), **kwargs)

    def x4(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 4x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-4x"), **kwargs)

    def x5(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 5x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-5x"), **kwargs)

    def x6(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 6x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-6x"), **kwargs)

    def x7(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 7x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-7x"), **kwargs)

    def x8(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 8x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-8x"), **kwargs)

    def x9(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 9x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-9x"), **kwargs)

    def x10(
        self, name: str, *, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 10x sized icon with the given attributes.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(name, class_=join(class_, "fa-10x"), **kwargs)


class StackFactory:
    """
    Factory that creates groups for stacking multiple icons on each-other.
    """

    def __init__(self, factory: Type[IElement]) -> None:
        """
        Initialization.

        Arguments:
            factory: The element to create icons from.
        """
        self._factory = factory

    def __call__(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a default-sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self._factory(*args, class_=join("fa-stack", class_), **kwargs)

    def default(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a default-sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=class_, **kwargs)

    def xs(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a extra-small-sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-xs"), **kwargs)

    def sm(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a small-sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-sm"), **kwargs)

    def lg(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a large-sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-lg"), **kwargs)

    def x2(
        self, *args, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 2x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(class_=join(class_, "fa-2x"), **kwargs)

    def x3(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 3x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-3x"), **kwargs)

    def x4(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 4x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-4x"), **kwargs)

    def x5(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 5x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-5x"), **kwargs)

    def x6(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 6x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-6x"), **kwargs)

    def x7(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 7x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-7x"), **kwargs)

    def x8(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 8x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-8x"), **kwargs)

    def x9(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 9x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-9x"), **kwargs)

    def x10(
        self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue
    ) -> IElement:
        """
        Creates a 10x sized icon with the given attributes.

        Positional arguments should be Font Awesome icons and they will become the children
        elements of the created stack element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return self(*args, class_=join(class_, "fa-10x"), **kwargs)
