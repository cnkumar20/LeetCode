package LeetCode;//import java.util.ArrayDeque;
//import java.util.ArrayList;
//import java.util.Queue;
//import java.util.Stack;
//
///**
// * Created by dexter on 11/1/16.
// */
//public class BFSandDFSTree {
//    public static void BFSTree(Tree inputQueue) {
//        Queue<Tree> buffQueue = new ArrayDeque<>();
//        if (inputQueue == null) return;
//
//        while (true) {
//            Queue<Tree> tempQueue = new ArrayDeque<>();
//
//            while (buffQueue != null) {
//
//                System.out.print(buffQueue + " ");
//                Tree temp = buffQueue.poll();
//                if (temp.left != null) {
//                    tempQueue.add(temp.left);
//                }
//                if (temp.right != null) {
//                    tempQueue.add(temp.right);
//                }
//            }
//
//            buffQueue.addAll(tempQueue);
//            System.out.println();
//
//            if (buffQueue.size() == 0)
//                break;
//
//        }
//    }
//
//
//    public static void DFSTree(Tree queueInput) {
//        Stack<Tree> stackInput = new Stack<>();
//        if(stackInput != null) return;
//
//        stackInput.add(queueInput);
//           Tree temp = queueInput;
//        while(stackInput.size() >0) {
//            if(temp.left != null) {
//                temp = temp.left;
//                stackInput.add(temp.left);
//                continue;
//            }
//            if(temp.left)
//            if(temp.right != null) {
//                stackInput.add(temp.left);
//                continue;
//            }
//
//
//        }
//
//    }
//}
