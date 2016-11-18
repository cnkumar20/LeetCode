package LeetCode;

import java.util.HashSet;

/**
 * Created by dexter on 10/26/16.
 */
public class LinkedListDeleteDups {
    public static class LinkedListNode {
        int data ;
        LinkedListNode next=null;
    }


    /**
     *  This method uses extra space to run O(n)
     * @param inputList
     */
    public static void deleteDups1(LinkedListNode inputList) {
        HashSet<Integer> set = new HashSet<>();
        LinkedListNode previous = null;

        while(inputList!=null) {
            if(set.contains(inputList.data)) {
                previous.next = inputList.next;
            }
            else {
                set.add(inputList.data);
                previous = inputList;
            }
            inputList = inputList.next;
        }
    }

    /**
     * Not using extra buffer but is bad perofrmance O(n^2)
     * @param inputList
     */
    public static void deleteDups2(LinkedListNode inputList) {
        if(inputList==null) return;
        LinkedListNode current = inputList;
        while(current!=null) {
            LinkedListNode runner = current;
            while(runner.next !=null) {
                if(runner.next.data == current.data){
                    runner.next = runner.next.next;
                }
                else {
                    runner = runner.next;
                }
            }

            current = current.next;
        }
    }

    public static void main(String[] args) {
        LinkedListNode input = new LinkedListNode();
        input.data = 1;
        input.next = new LinkedListNode();
        input.next.data = 2;
        input.next.next = new LinkedListNode();
        input.next.next.data = 1;
        deleteDups1(input);
        LinkedListNode cur = input;
        while(cur != null) {
            System.out.print(cur.data +"---");
            cur = cur.next;
        }
    }

}
