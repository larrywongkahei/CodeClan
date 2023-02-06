public class Main {

    public static void main(String[] args) {
        Planet mars = new Planet("mars", 908973);
        System.out.println(String.format("%s, is %,.2f", mars.get_name(), mars.get_size()));
        mars.explode();

    }

};