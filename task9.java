package com.petehouston.tutorial.java;
import java.util.Scanner;
import java.lang.String;

public class HelloWorld {

    public static void main(String[] args) {


        homeWork();

    }


    static void homeWork(){

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] numbers = new int[n];
        int max=0, min=0;
        for (int i=0; i<n; i++){
            numbers[i] = scan.nextInt();
        }

        for (int j=0; j<n; j++){
            if(numbers[j]>max){
                max = numbers[j];
            }
        }

        for (int k=0; k<n; k++){
            if(numbers[k]<min){
                min = numbers[k];
            }
        }
        int maxIndex = maxindexOf(max, numbers);
        int minIndex = minindexOf(min, numbers);

        int result = 0;
        int interMul = 1;
        for (int t=0; t<n; t++){
            if(numbers[t]>0) result += numbers[t];
        }

        if (maxIndex > minIndex){
            for (int l=minIndex+1; l<maxIndex; l++){
                interMul *= numbers[l];
            }
        }
        else if (maxIndex < minIndex){
            for (int l=minIndex; l>maxIndex+1; l--){
                interMul *= numbers[l];
            }
        }

        System.out.printf("\n%d %d",result,interMul);
    }

    private static int maxindexOf(int max, int[] numbers) {
        for (int i=0;i<numbers.length; i++){
            if (numbers[i]==max){
                return i;
            }
        }
        return -1;
    }
    private static int minindexOf(int min, int[] numbers){
        for (int i=0; i<numbers.length; i++){
            if(numbers[i]==min){
                return i;
            }
        }
        return -1;
    }
}
