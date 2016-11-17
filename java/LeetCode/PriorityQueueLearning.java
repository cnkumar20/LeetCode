package LeetCode;

import java.util.HashMap;
import java.util.PriorityQueue;

/**
 * Created by dexter on 10/30/16.
 */
public class PriorityQueueLearning {

    public static void main(String[] args) {
        int[] ia = { 1, 10, 5, 3, 4, 7, 6, 9, 8 };
        PQSort pqsort = new PQSort();
        PriorityQueue<Integer> pq = new PriorityQueue<>(10,pqsort);
        for(int a : ia) {
            pq.offer(a);
        }


        System.out.println("Priority Queue  :"+pq);


        while(!pq.isEmpty()) {
            System.out.println(pq.poll());
        }

        String[] ip = {"Kumar","and","his","friends"};

        PriorityQueue<String> pq1 = new PriorityQueue<>(10,pqsort);

        for(String a : ip) {
            pq1.offer(a);
        }

        System.out.println("Priority Queue  :"+pq1);


        HashMap<String,PriorityQueue> check = new HashMap<>();
        check.put("String",pq1);
        check.put("Integer",pq);

        System.out.println(check.get("String"));

    }
}
