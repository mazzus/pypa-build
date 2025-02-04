import sys


if sys.version_info < (3, 8):
    import importlib_metadata as metadata
elif sys.version_info >= (3, 10, 2):
    from importlib import metadata
else:
    try:
        import importlib_metadata as metadata
    except ModuleNotFoundError:
        # helps bootstrapping when dependencies aren't installed
        from importlib import metadata

__all__ = ['metadata']
