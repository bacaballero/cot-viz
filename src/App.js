import React from 'react'
import { Line } from 'react-chartjs-2'
import * as jsonData from './json_data.json'
import { useState, useEffect } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const data = jsonData

function App() {
  const [commodity, setCommodity] = useState('#2 HEATING OIL- NY HARBOR-ULSD - NEW YORK MERCANTILE EXCHANGE')
  const [selectedCommodityData, setSelectedCommodityData] = useState([data.data.filter(future => future.name === commodity)])

  useEffect(() => {
    setSelectedCommodityData(data.data.filter(future => future.name === commodity))
  }, [commodity])

  const handleChange = (event) => {
    setCommodity(event.target.value) 
  }

  return (
    <div>
      <label>
        Select a commodity 
        <select value={commodity} onChange={handleChange}>
          {data.data.map(future =>
            <option key={future.name} value={future.name}>{future.name}</option>)}
        </select>
      </label>
      <h1>Commitment of Traders Data</h1>
        <div key={selectedCommodityData[0].name}>
          <Line options={{responsive: true, layout: {padding: 80} , plugins: {title: {display: true, text: selectedCommodityData[0].name}}}} 
            data={
              {
                labels: selectedCommodityData[0].dates,
                datasets: [
                  {
                    label: 'Commercial Hedgers',
                    data: selectedCommodityData[0].commercial,
                    borderColor: 'green',
                    backgroundColor: 'green',
                    borderJoinStyle: 'round',
                    pointStyle: 'line',
                    pointBorderWidth: 0,
                    
                  },
                  {
                    label: 'Small Traders',
                    data: selectedCommodityData[0]['non reporting'],
                    borderColor: 'blue',
                    backgroundColor: 'blue',
                    borderJoinStyle: 'round',
                    pointStyle: 'line',
                    pointBorderWidth: 0,
                  },
                  {
                    label: 'Large Traders',
                    data: selectedCommodityData[0]['non commercial'],
                    borderColor: 'red',
                    backgroundColor: 'red',
                    borderJoinStyle: 'round',
                    pointStyle: 'line',
                    pointBorderWidth: 0
                  },
                ]
              }
            }/>
        </div>
    </div>
  );
}


export default App;

/// <Line data={{labels: future.dates, datasets: [{label: future.name, data: future.commercial}]}}/>