import React from 'react'
import { Line } from 'react-chartjs-2'
import * as jsonData from './json_data.json'
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
console.log(data.data.map(n => n.name))

const names = data.data.map(futures => futures.name)
const dates = data.data.map(futures => futures.dates)

function App() {
  return (
    <div>
      <h1>Commitment of Traders Data</h1>
      {data.data.map(future => 
        <div key={future.name}>
          <Line options={{responsive: true, plugins: {title: {display: true, text: future.name}}}} 
            data={
              {
                labels: future.dates,
                datasets: [
                  {
                    label: 'Commercial Hedgers',
                    data: future.commercial,
                    borderColor: 'green',
                    backgroundColor: 'green'
                  },
                  {
                    label: 'Small Traders',
                    data: future['non reporting'],
                    borderColor: 'blue',
                    backgroundColor: 'blue'
                  },
                  {
                    label: 'Large Traders',
                    data: future['non commercial'],
                    borderColor: 'red',
                    backgroundColor: 'red'
                  },
                ]
              }
            }/>
        </div>
      )}
    </div>
  );
}


export default App;

/// <Line data={{labels: future.dates, datasets: [{label: future.name, data: future.commercial}]}}/>