import java.util.ArrayList;

public class Bedroom extends Room{

    private int roomNumber;
    private int capacity;

    private RoomType roomType;

    public Bedroom(ArrayList<String> guest,RoomType roomType, int roomNumber) {
        super(guest, roomType.getCapacity());
        this.roomNumber = roomNumber;
        this.capacity = roomType.getCapacity();

    }
}
