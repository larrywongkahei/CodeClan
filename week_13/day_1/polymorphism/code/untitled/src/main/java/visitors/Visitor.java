package visitors;

import attractions.Attraction;

import java.util.ArrayList;

public class Visitor {

    public int age;
    public int height;
    public double money;

    public ArrayList<Attraction> visitedAttractions;


    public Visitor (int age, int height, double money){
        this.age = age;
        this.height = height;
        this.money = money;
        this.visitedAttractions = new ArrayList<>();
    }

    public int getAge() {
        return age;
    }

    public int getHeight() {
        return height;
    }

    public double getMoney() {
        return money;
    }

    public void addAttraction(Attraction attraction){
        visitedAttractions.add(attraction);
    }
}
