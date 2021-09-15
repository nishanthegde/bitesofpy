import ast

from typing import Any, Dict


class AstPrinter(ast.NodeVisitor):
    def __init__(self, show_empty: bool = True) -> None:
        """Initialize the object

        Arguments:
        - show_empty: when is True do not show nodes that are None,
             are empty lists, are empty string
        """

        super().__init__()
        self.SHOW_EMTPY = show_empty

    def _is_node(self, obj: Any) -> bool:
        """return True if obj is an ast.AST object"""
        return isinstance(obj, ast.AST)

    def _is_list_of_nodes(self, obj: Any) -> bool:
        """return True if obj is a list ast.AST objects"""
        return isinstance(obj, list) and len(obj) > 0 and self._is_node(obj[0])

    def _get_name(self, obj: Any) -> str:
        """return obj class name"""
        return obj.__class__.__name__

    def _is_empty(self, obj: Any) -> bool:
        """return True if obj is an empty list, empty string, or None"""
        return (isinstance(obj, list) and len(obj) == 0) or obj == "" or obj is None

    def _get_attrs(self, node: ast.AST) -> Dict[str, Any]:
        """look simple attributes, and returns them as a dictionary where
        key is the attribute name, and value the attribute value
        """
        d = {}
        for attr_name, attr_value in ast.iter_fields(node):
            if (
                    not self._is_node(attr_value)
                    and not self._is_list_of_nodes(attr_value)
                    and (self.SHOW_EMTPY or not self._is_empty(attr_value))
            ):
                d[attr_name] = attr_value

        return d

    def _get_children(self, node: ast.AST) -> Dict[str, Any]:
        """look for attributes being either nodes, or list of nodes,
        and returns them as a dictionary where key is the attribute name,
        and value the attribute value
        """
        d = {}
        for attr_name, attr_value in ast.iter_fields(node):
            if self._is_node(attr_value) or self._is_list_of_nodes(attr_value):
                d[attr_name] = attr_value
        return d

    def visit(self, node, ws_count=0):
        """trigger visit"""

        # define your logic to print the content of the tree
        #
        # you can use self._get_attrs() and self._get_children() to
        # separate the attributes in the two required types

        print('{0}{1}{2}'.format(ws_count * ' ', self._get_name(node), '()'))

        # print(self._get_attrs(node))
        attr_dict = self._get_attrs(node)
        i = 0
        for k in sorted(attr_dict):
            if i == 0:
                ws_count += 3
            if isinstance(attr_dict[k], str):
                print('{0}{1}{2}{3} \'{4}\''.format(ws_count * ' ', '.', k, ':', attr_dict[k]))
            else:
                print('{0}{1}{2}{3} {4}'.format(ws_count * ' ', '.', k, ':', attr_dict[k]))
            i += 1

        # print(self._get_children(node))
        child_dict = self._get_children(node)
        for k in child_dict:
            print('{0}{1}{2}{3}'.format(ws_count * ' ', '.', k, ':'))
            if self._is_list_of_nodes(child_dict[k]):
                for n in child_dict[k]:
                    ws_count += 3
                    self.visit(n, ws_count)
            elif self._is_node(child_dict[k]):
                ws_count += 3
                self.visit(child_dict[k], ws_count)
            # print(k, v, self._is_node(k), self._get_name(v),self._is_list_of_nodes(v))


def main():
    print("thank you for looking after Mama and Nai'a!")


if __name__ == "__main__":
    main()
    code = """
one_plus_two = 1+2
one_plus_two+10
"""
    CODE_ONE_LINE = """
one_plus_two = 1+2
"""

    CODE_ONE_LINE_AST = """
    Module()
       .type_ignores: []
       .body:
          Assign()
             .type_comment: None
             .targets:
                Name()
                   .id: 'one_plus_two'
                   .ctx:
                      Store()
             .value:
                BinOp()
                   .left:
                      Constant()
                         .kind: None
                         .value: 1
                   .op:
                      Add()
                   .right:
                      Constant()
                         .kind: None
                         .value: 2
    """

    tree = ast.parse(CODE_ONE_LINE)
    print(ast.dump(tree))
    vst = AstPrinter()
    vst.visit(tree)
    print(CODE_ONE_LINE_AST)