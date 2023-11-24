import java.util.LinkedList;
import java.util.Queue;

public class BridgeTruck {

    private final Queue<Truck> trucks;

    private final Queue<Truck> bridge;

    private final int bridgeLength;

    private final int maxWeight;

    private int currentWeight;

    
    private static class Truck {

        private final int weight;

        private int position;

        public Truck(final int weight, final int position) {
            this.weight = weight;
            this.position = position;
        }

        public void move() {
            this.position++;
        }

        public int getWeight() {
            return weight;
        }
    }

    public BridgeTruck(final int bridge_length, int weight, int[] truck_weights) {
        this.trucks = new LinkedList<>();
        this.bridge = new LinkedList<>();
        this.maxWeight = weight;
        this.bridgeLength = bridge_length;
        this.currentWeight = 0;
        mapTrucks(truck_weights);
    }

    private void mapTrucks(final int[] truckWeights) {
        for (int truckWeight : truckWeights) {
            trucks.offer(new Truck(truckWeight, 0));
        }
    }

    public int sol() {
        int answer = 0;

        while (!bridge.isEmpty() || !trucks.isEmpty()) {
            Truck truck = trucks.peek();

            if (bridge.isEmpty() || canPassable(truck)) {
                bridge.offer(trucks.poll());
                currentWeight += truck.getWeight();
            }
            moveTrucksOnBridge();
            updateTrucks();
            answer++;
        }
        return answer + 1;
    }

    private boolean canPassable(final Truck truck) {
        return isPassableLength() && isPassableWeight(truck);
    }

    private boolean isPassableLength() {
        return bridge.size() < bridgeLength;
    }

    private boolean isPassableWeight(final Truck truck) {
        return truck != null && currentWeight + truck.weight <= maxWeight;
    }

    private void moveTrucksOnBridge() {
        if (!bridge.isEmpty()) {
            bridge.forEach(Truck::move);
        }
    }

    private void updateTrucks() {
        if (!bridge.isEmpty()) {
            if (bridge.peek().position >= bridgeLength) {
                Truck truck = bridge.poll();
                currentWeight -= truck.getWeight();
            }
        }
    }
}


class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        BridgeTruck bridgeTruck = new BridgeTruck(
            bridge_length, weight, truck_weights);
        return bridgeTruck.sol();
    }
}