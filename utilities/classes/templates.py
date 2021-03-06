# Classes to represent metadata for command line tools.
from collections import OrderedDict
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


class MetadataBase:
    """Will factor stuff out to here eventually."""

    _init_metadata = OrderedDict()

    def __init__(self):
        pass

    def mk_file(self, file_path):
        pass

    def update_file(self, file_path):
        raise NotImplementedError


class ToolMetadata(MetadataBase):
    """Class to represent metadata for a command line tool."""
    _init_metadata = OrderedDict([
        ('name', None),
        ('softwareVersion', None),
        ('version', None),
        ('description', None),
        ('codeRepository', dict([('name', None), ('URL', None)])),
        ('license', None),
        ('WebSite', [{'name': None, 'description': None, 'URL': None}]),
        ('contactPoint', [{'name': None, 'email': None, 'identifier': None}]),
        ('publication', [{'identifier': None, 'headline': None}]),
        ('keywords', []),
        ('alternateName', []),
        ('creator', [{'name': None, 'email': None, 'identifier': None}]),
        ('programmingLanguage', []),
        ('datePublished', None),
        ('downloadURL', None)
    ])

    @classmethod
    def _metafile_keys(cls):
        return list(cls._init_metadata.keys())


    def __init__(self, **kwargs):
        super().__init__()
        for k, v in ToolMetadata._init_metadata.items():
            setattr(self, k, v)

        for k, v in kwargs.items():
            if not k in ToolMetadata._init_metadata:
                raise AttributeError(f"{k} is not a valid key for ToolMetadata")
            setattr(self, k, v)
        return

    def mk_file(self, file_path):
        keys = ToolMetadata._metafile_keys()
        meta_map = CommentedMap()
        for key in keys:
            meta_map[key] = getattr(self, key)
        yaml = YAML()
        yaml.default_flow_style = False
        yaml.indent(mapping=2, sequence=4, offset=2)
        with open(file_path, 'w') as yaml_file:
            yaml.dump(meta_map, yaml_file)
        return


class SubtoolMetadata(MetadataBase):
    _init_metadata = OrderedDict([
        ('applicationSuite', {'name': None, 'softwareVersion': None, 'identifier': None}),
        ('name', None),
        ('version', None),
        ('description', None),
        ('keywords', []),
        ('alternateName', []),
    ])

    @classmethod
    def _metafile_keys(cls):
        return list(cls._init_metadata.keys())

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in self._init_metadata.items():
            setattr(self, k, v)

        for k, v in kwargs.items():
            if not k in self._init_metadata:
                raise KeyError(f"{k} is not a valid key for ToolMetadata")
            setattr(self, k, v)
        return

    def mk_file(self, file_path):
        keys = SubtoolMetadata._metafile_keys()
        meta_map = CommentedMap()
        for key in keys:
            meta_map[key] = getattr(self, key)
        yaml = YAML()
        yaml.default_flow_style = False
        yaml.indent(mapping=2, sequence=4, offset=2)
        with open(file_path, 'w') as yaml_file:
            yaml.dump(meta_map, yaml_file)
        return


class ParentToolMetadata(MetadataBase):
    _init_metadata = dict([
        ('name', None),
        ('softwareVersion', None),
        ('featureList', []),
        ('description', None),
        ('codeRepository', dict([('name', None), ('URL', None)])),
        ('license', None),
        ('WebSite', [{'name': None, 'description': None, 'URL': None}]),
        ('contactPoint', [{'name': None, 'email': None, 'identifier': None}]),
        ('publication', [{'identifier': None, 'headline': None}]),
        ('keywords', []),
        ('alternateName', []),
        ('creator', [{'name': None, 'email': None, 'identifier': None}]),
        ('programmingLanguage', []),
        ('datePublished', None),
        ('downloadURL', None)
    ])

    @classmethod
    def _metafile_keys(cls):
        return list(cls._init_metadata.keys())

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in self._init_metadata.items():
            setattr(self, k, v)

        for k, v in kwargs.items():
            if not k in self._init_metadata:
                raise KeyError(f"{k} is not a valid key for ToolMetadata")
            setattr(self, k, v)
        return

    def mk_file(self, file_path):
        keys = ParentToolMetadata._metafile_keys()
        meta_map = CommentedMap()
        for key in keys:
            meta_map[key] = getattr(self, key)
        yaml = YAML()
        yaml.default_flow_style = False
        yaml.indent(mapping=2, sequence=4, offset=2)
        with open(file_path, 'w') as yaml_file:
            yaml.dump(meta_map, yaml_file)
        return

