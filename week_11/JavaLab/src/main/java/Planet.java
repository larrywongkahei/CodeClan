public class Planet {
    private String name;
    private double size;

    public Planet(String name, double size){
        this.name = name;
        this.size = size;


    }

    public String get_name(){
        return this.name;
    }

    public double get_size(){
        return this.size;
    }

    public void explode(){
        System.out.println(String.format("Boom! %s has exploded", this.name));
    }

}
