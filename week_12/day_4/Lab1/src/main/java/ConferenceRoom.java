import java.util.ArrayList;

public class ConferenceRoom extends Room{

    private String name;

    private RoomType roomType

    public ConferenceRoom(ArrayList guest, RoomType roomType, String name) {
        super(guest, roomType.getCapacity());
        this.name = name;
    }
}