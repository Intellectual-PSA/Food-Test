class Food:
    def __init__(self, name, initial_quality):
        self.name = name
        self.initial_quality = initial_quality
        self.current_quality = initial_quality

    def check_freshness(self):
        """
        Let's assume that this function can somehow access sensor data and
        updates the current quality of the food item.
        """
        sensor_data = self.get_sensor_data()
        self.current_quality = self.process_sensor_data(sensor_data)

        if self.current_quality < 0.5 * self.initial_quality:
            return False
        else:
            return True

    def get_sensor_data(self):
        """
        This is a placeholder for function that would collect data from a sensor.
        """
        # Since we don't have actual sensors, we'll simulate a quality decrease by returning a random number
        import random
        return random.uniform(0, 1)

    def process_sensor_data(self, sensor_data):
        """
        This is a placeholder for function that would process the sensor data.
        """
        # For this example, let's just return the sensor data
        return sensor_data

# Example usage:

banana = Food("Banana", initial_quality=1.0)

if banana.check_freshness():
    print(f"The {banana.name} is fresh.")
else:
    print(f"The {banana.name} is not fresh.")
