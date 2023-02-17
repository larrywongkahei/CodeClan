public class FlightManager {

    public static double getBaggageWeightForPassenger(Flight flight){
        return (flight.getTotalWeight()/2) / flight.getCapacity();
    }

    public static double getBaggageForPasserngers(Flight flight){
        return flight.getTotalWeight()/2 ;
    }

    public static double getBaggageRemains(Flight flight){
        return ((flight.getTotalWeight()/2) / flight.getCapacity()) * flight.getSeatsBooked();
    }
}
