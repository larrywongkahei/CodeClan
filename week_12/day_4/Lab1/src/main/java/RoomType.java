public enum RoomType {
    SINGLE(1),
    DOUBLE(2),
    SUITE(5);

    private final int capacity;

    RoomType (int capacity){
        this.capacity = capacity;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
