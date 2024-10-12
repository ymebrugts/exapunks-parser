# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ExapunksSolution(KaitaiStruct):

    class WinValueType(Enum):
        cycles = 0
        size = 1
        activity = 2

    class EditorDisplayStatus(Enum):
        unrolled = 0
        collapsed = 1

    class MemoryScope(Enum):
        global_scope = 0
        local_scope = 1
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\xF0\x03\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\xF0\x03\x00\x00", self.magic, self._io, u"/seq/0")
        self.file_id = ExapunksSolution.Pstr(self._io, self, self._root)
        self.name = ExapunksSolution.Pstr(self._io, self, self._root)
        self.competition_wins = self._io.read_u4le()
        self.redshift_program_size = self._io.read_u4le()
        self.win_stats_count = self._io.read_u4le()
        self.win_stats = []
        for i in range(self.win_stats_count):
            self.win_stats.append(ExapunksSolution.WinValuePair(self._io, self, self._root))

        self.exa_instances_count = self._io.read_u4le()
        self.exa_instances = []
        for i in range(self.exa_instances_count):
            self.exa_instances.append(ExapunksSolution.ExaInstance(self._io, self, self._root))


    class Pstr(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u4le()
            self.string = (self._io.read_bytes(self.length)).decode(u"ASCII")


    class WinValuePair(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(ExapunksSolution.WinValueType, self._io.read_u4le())
            self.value = self._io.read_u4le()


    class ExaInstance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._unnamed0 = self._io.read_bytes(1)
            if not self._unnamed0 == b"\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x0A", self._unnamed0, self._io, u"/types/exa_instance/seq/0")
            self.name = ExapunksSolution.Pstr(self._io, self, self._root)
            self.code = ExapunksSolution.Pstr(self._io, self, self._root)
            self.editor_display_status = KaitaiStream.resolve_enum(ExapunksSolution.EditorDisplayStatus, self._io.read_u1())
            self.memory_scope = KaitaiStream.resolve_enum(ExapunksSolution.MemoryScope, self._io.read_u1())
            self.bitmap = self._io.read_bytes(100)



