package staff.management;
import staff.management.Manager;

public class Director extends Manager {

    private double budget;

    public Director(String name, String niNumber, Integer salary, String deptName, double budget) {
        super(name, niNumber, salary, deptName);
        this.budget = budget;
    }


    public double getBudget() {
        return budget;
    }
    @Override
    public double payBonus(){
        return salary * 0.02;
    }
}
