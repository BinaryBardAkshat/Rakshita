// CarData.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CarData = () => {
  const [carData, setCarData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5050');
        setCarData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Car Data</h1>
      <table>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>RPM</th>
            <th>Vehicle Speed</th>
            <th>Coolant Temp</th>
            <th>Throttle Pos</th>
            <th>Engine Load</th>
            <th>License Plate</th>
            <th>Distance</th>
          </tr>
        </thead>
        <tbody>
          {carData.map((data, index) => (
            <tr key={index}>
              <td>{data.timestamp}</td>
              <td>{data.rpm}</td>
              <td>{data.vehicle_speed}</td>
              <td>{data.coolant_temp}</td>
              <td>{data.throttle_pos}</td>
              <td>{data.engine_load}</td>
              <td>{data.license_plate}</td>
              <td>{data.distance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CarData;
