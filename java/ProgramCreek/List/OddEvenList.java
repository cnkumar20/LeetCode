package ProgramCreek.List;

import ProgramCreek.DataStructure.*;


/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class OddEvenList {
  public static ListNode oddEvenList(ListNode head) {
    if(head == null || head.next == null) {
      return head;
    }


    ListNode odd = head;
    ListNode even = head.next;
    ListNode evenHead = even;


    while(even != null && even.next != null) {
      odd.next = even.next;
      odd = odd.next;

      even.next = odd.next;
      even = even.next;

    }

    odd.next = evenHead;
    return head;
  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    oddEvenList(head);
  }
}
