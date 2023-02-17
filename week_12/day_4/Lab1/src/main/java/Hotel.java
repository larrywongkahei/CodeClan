import java.util.ArrayList;

public class Hotel {
    private ArrayList<Bedroom> bedroomList;
    private ArrayList<ConferenceRoom> conferenceRoomList;

    public Hotel(ArrayList<Bedroom> bedrooms, ArrayList<ConferenceRoom> conferenceRooms) {
        this.bedroomList = bedrooms;
        this.conferenceRoomList = conferenceRooms;
    }

    public ArrayList<Bedroom> getBedroomList() {
        return bedroomList;
    }

    public ArrayList<ConferenceRoom> getConferenceRoomList() {
        return conferenceRoomList;
    }

    public void checkInGuest(RoomType room, String decision){
        if (decision == in){

        }
    }
}
