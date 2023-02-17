public class Car implements Convert{
    public String name;
    public int age;

    public Car(String name, int age){
        this.name = name;
        this.age = age;
    }

    public String getName(){
        return name;
    }

    public String convert(){
        return "Car data";
    }
}
