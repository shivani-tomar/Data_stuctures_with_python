import linked_list_create_node as cn
import linked_list_traverse as trav
import linked_list_search_node as sear
import linked_list_insert_node as ins
import linked_list_delete_node as dele
import config as con


def main():
    print("I am in main accessing head from this file")
    linked_list_cre = cn.linkedList()
    print(con.head)
    linked_list_cre.insertNode("1")
    linked_list_cre.insertNode("2")
    linked_list_cre.insertNode("3")
    linked_list_cre.insertNode("4")
    linked_list_cre.insertNode("5")
    linked_list_cre.insertNode("6")
    linked_list_cre.insertNode("7")

    linked_list_trav = trav.traverse()
    linked_list_trav.trackLinkedlist()

    linked_list_sear = sear.search()
    linked_list_sear.searchLinkedlist("8")

    linked_list_ins = ins.insert()
    linked_list_ins.insertAtFirst("0")
    linked_list_trav.trackLinkedlist()
    linked_list_ins.insertAtLast("8")
    linked_list_trav.trackLinkedlist()
    linked_list_ins.insertAtPosition(9,"9")
    linked_list_ins.insertAtPosition(10,"10")

    linked_list_trav.trackLinkedlist()

    linked_list_dele = dele.delete()
    linked_list_dele.firstNodeDeletion()
    linked_list_trav.trackLinkedlist()

    linked_list_dele.lastNodeDeletion()
    linked_list_trav.trackLinkedlist()

    linked_list_dele.deletionByPosition(6)
    linked_list_trav.trackLinkedlist()

    linked_list_dele.deletionByData("7")
    linked_list_trav.trackLinkedlist()

    linked_list_dele.deletionByPosition(11)
    linked_list_trav.trackLinkedlist()










if __name__ == "__main__":
    # print("I am in main")
    # print(__name__)
    main()