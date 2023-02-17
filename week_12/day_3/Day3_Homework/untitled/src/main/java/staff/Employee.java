package staff;

public abstract class Employee {

    protected String name;
    protected String niNumber;
    protected double salary;

    public Employee(String name,String niNumber, Integer salary){
        this.name = name;
        this.niNumber = niNumber;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public String getNiNumber() {
        return niNumber;
    }

    public double getSalary() {
        return salary;
    }

    public void raiseSalary(double amount){
        if (amount >= 0){salary += amount;}
    }

    public double payBonus(){
        return salary / 100;
    }

    public void changeName(String newName){
        if (newName != null){this.name = newName;}
    }
}
