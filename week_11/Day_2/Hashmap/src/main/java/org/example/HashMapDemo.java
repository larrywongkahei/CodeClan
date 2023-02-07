package org.example;

import java.util.HashMap;

public class HashMapDemo {

    public static void main(String[] args){
        HashMap<String, Integer> ages = new HashMap<>();

        ages.put("Alice", 32);
        ages.put("Bessy", 23);
        ages.put("Olly", 52);
        int aliceAge = ages.get("Alice");

        String output = String.format("Alice's age is %d", aliceAge);
        System.out.println(output);
    }

}
