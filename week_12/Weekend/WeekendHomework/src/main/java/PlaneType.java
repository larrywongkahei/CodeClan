public enum PlaneType {
    BOEING747(3, 2400),
    BOEING777(56, 2500);

    private final int capacity;
    private final double totalWeight;

    PlaneType(int capacity, double totalWeight) {
        this.capacity = capacity;
        this.totalWeight = totalWeight;
    }

    public int getCapacity(){
        return this.capacity;
    }

    public double getTotalWeight(){
        return this.totalWeight;
    }
}
