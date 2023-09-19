from _typeshed import Incomplete
from typing import Any

from sqlalchemy.sql import ClauseElement

from ...engine import default
from ...sql import compiler, sqltypes
from ...types import (
    BLOB as BLOB,
    CHAR as CHAR,
    CLOB as CLOB,
    FLOAT as FLOAT,
    INTEGER as INTEGER,
    NCHAR as NCHAR,
    NVARCHAR as NVARCHAR,
    TIMESTAMP as TIMESTAMP,
    VARCHAR as VARCHAR,
)

RESERVED_WORDS: Any
NO_ARG_FNS: Any

class RAW(sqltypes._Binary):
    __visit_name__: str

OracleRaw = RAW

class NCLOB(sqltypes.Text):
    __visit_name__: str

class VARCHAR2(VARCHAR):
    __visit_name__: str

NVARCHAR2 = NVARCHAR

class NUMBER(sqltypes.Numeric, sqltypes.Integer):
    __visit_name__: str
    def __init__(
        self, precision: Incomplete | None = None, scale: Incomplete | None = None, asdecimal: Incomplete | None = None
    ) -> None: ...
    def adapt(self, impltype): ...

class DOUBLE_PRECISION(sqltypes.Float):
    __visit_name__: str

class BINARY_DOUBLE(sqltypes.Float):
    __visit_name__: str

class BINARY_FLOAT(sqltypes.Float):
    __visit_name__: str

class BFILE(sqltypes.LargeBinary):
    __visit_name__: str

class LONG(sqltypes.Text):
    __visit_name__: str

class DATE(sqltypes.DateTime):
    __visit_name__: str

class INTERVAL(sqltypes.NativeForEmulated, sqltypes._AbstractInterval):
    __visit_name__: str
    day_precision: Any
    second_precision: Any
    def __init__(self, day_precision: Incomplete | None = None, second_precision: Incomplete | None = None) -> None: ...
    def as_generic(self, allow_nulltype: bool = False): ...
    def coerce_compared_value(self, op, value): ...

class ROWID(sqltypes.TypeEngine):
    __visit_name__: str

class _OracleBoolean(sqltypes.Boolean):
    def get_dbapi_type(self, dbapi): ...

colspecs: Any
ischema_names: Any

class OracleTypeCompiler(compiler.GenericTypeCompiler):
    def visit_datetime(self, type_, **kw): ...
    def visit_float(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_INTERVAL(self, type_, **kw): ...
    def visit_LONG(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_DOUBLE_PRECISION(self, type_, **kw): ...
    def visit_BINARY_DOUBLE(self, type_, **kw): ...
    def visit_BINARY_FLOAT(self, type_, **kw): ...
    def visit_FLOAT(self, type_, **kw): ...
    def visit_NUMBER(self, type_, **kw): ...
    def visit_string(self, type_, **kw): ...
    def visit_VARCHAR2(self, type_, **kw): ...
    def visit_NVARCHAR2(self, type_, **kw): ...
    visit_NVARCHAR: Any
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_big_integer(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_RAW(self, type_, **kw): ...
    def visit_ROWID(self, type_, **kw): ...

class OracleCompiler(compiler.SQLCompiler):
    compound_keywords: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def visit_mod_binary(self, binary, operator, **kw): ...
    def visit_now_func(self, fn, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def get_cte_preamble(self, recursive): ...
    def get_select_hint_text(self, byfroms): ...
    def function_argspec(self, fn, **kw): ...
    def visit_function(self, func, **kw): ...
    def visit_table_valued_column(self, element, **kw): ...
    def default_from(self): ...
    def visit_join(self, join, from_linter: Incomplete | None = None, **kwargs): ...  # type: ignore[override]
    def visit_outer_join_column(self, vc, **kw): ...
    def visit_sequence(self, seq, **kw): ...
    def get_render_as_alias_suffix(self, alias_name_text): ...
    has_out_parameters: bool
    def returning_clause(self, stmt, returning_cols): ...
    def translate_select_structure(self, select_stmt, **kwargs): ...
    def limit_clause(self, select, **kw): ...
    def visit_empty_set_expr(self, type_): ...
    def for_update_clause(self, select, **kw): ...
    def visit_is_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_is_not_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw): ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw): ...

class OracleDDLCompiler(compiler.DDLCompiler):
    def define_constraint_cascades(self, constraint): ...
    def visit_drop_table_comment(self, drop): ...
    def visit_create_index(self, create): ...
    def post_create_table(self, table): ...
    def get_identity_options(self, identity_options): ...
    def visit_computed_column(self, generated): ...
    def visit_identity_column(self, identity, **kw): ...

class OracleIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any
    illegal_initial_characters: Any
    def format_savepoint(self, savepoint): ...

class OracleExecutionContext(default.DefaultExecutionContext):
    def fire_sequence(self, seq, type_): ...

class OracleDialect(default.DefaultDialect):
    name: str
    supports_statement_cache: bool
    supports_alter: bool
    supports_unicode_statements: bool
    supports_unicode_binds: bool
    max_identifier_length: int
    supports_simple_order_by_label: bool
    cte_follows_insert: bool
    supports_sequences: bool
    sequences_optional: bool
    postfetch_lastrowid: bool
    default_paramstyle: str
    colspecs: Any
    ischema_names: Any
    requires_name_normalize: bool
    supports_comments: bool
    supports_default_values: bool
    supports_default_metavalue: bool
    supports_empty_insert: bool
    supports_identity_columns: bool
    statement_compiler: Any
    ddl_compiler: Any
    type_compiler: Any
    preparer: Any
    reflection_options: Any
    construct_arguments: Any
    use_ansi: Any
    optimize_limits: Any
    exclude_tablespaces: Any
    def __init__(
        self,
        use_ansi: bool = True,
        optimize_limits: bool = False,
        use_binds_for_limits: Incomplete | None = None,
        use_nchar_for_unicode: bool = False,
        exclude_tablespaces=("SYSTEM", "SYSAUX"),
        **kwargs,
    ) -> None: ...
    implicit_returning: Any
    def initialize(self, connection) -> None: ...
    def do_release_savepoint(self, connection, name) -> None: ...
    def get_isolation_level(self, connection) -> None: ...
    def get_default_isolation_level(self, dbapi_conn): ...
    def set_isolation_level(self, connection, level) -> None: ...
    def has_table(self, connection, table_name, schema: Incomplete | None = None): ...  # type: ignore[override]
    def has_sequence(self, connection, sequence_name, schema: Incomplete | None = None): ...  # type: ignore[override]
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, schema: Incomplete | None = None, **kw): ...
    def get_temp_table_names(self, connection, **kw): ...
    def get_view_names(self, connection, schema: Incomplete | None = None, **kw): ...
    def get_sequence_names(self, connection, schema: Incomplete | None = None, **kw): ...
    def get_table_options(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_columns(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_table_comment(
        self, connection, table_name, schema: Incomplete | None = None, resolve_synonyms: bool = False, dblink: str = "", **kw
    ): ...
    def get_indexes(
        self, connection, table_name, schema: Incomplete | None = None, resolve_synonyms: bool = False, dblink: str = "", **kw
    ): ...
    def get_pk_constraint(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_foreign_keys(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_unique_constraints(self, connection, table_name, schema: Incomplete | None = None, **kw): ...
    def get_view_definition(
        self, connection, view_name, schema: Incomplete | None = None, resolve_synonyms: bool = False, dblink: str = "", **kw
    ): ...
    def get_check_constraints(
        self, connection, table_name, schema: Incomplete | None = None, include_all: bool = False, **kw
    ): ...

class _OuterJoinColumn(ClauseElement):
    __visit_name__: str
    column: Any
    def __init__(self, column) -> None: ...
