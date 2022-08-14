import React from "react";
import { Line } from "react-chartjs-2";
import * as jsonData from "./json_data.json";
import * as priceData from "./price_data.json";
import { useState, useEffect } from "react";
import { Container, Dropdown, Navbar, NavDropdown, Nav } from "react-bootstrap";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const data = jsonData;
const futurePriceData = priceData;

function App() {
  const [commodity, setCommodity] = useState(
    "E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE"
  );
  const [selectedCommodityData, setSelectedCommodityData] = useState([
    data.data.filter((future) => future.name === commodity),
  ]);

  const [selectedFuturePriceData, setSelectedFuturePriceData] = useState([
    futurePriceData.data.filter((future) => future.name === commodity),
  ]);

  useEffect(() => {
    setSelectedCommodityData(
      data.data.filter((future) => future.name === commodity)
    );
    setSelectedFuturePriceData(
      futurePriceData.data.filter((future) => future.name === commodity)
    );
  }, [commodity]);

  const handleSelect = (event) => {
    setCommodity(event.target.text);
  };

  return (
    <div>
      <Navbar bg="dark" variant="dark" className="mb-3">
        <Container>
          <Navbar.Brand className="text-info">CFTC COT Data</Navbar.Brand>
        </Container>
        <Nav className="me-auto">
          <NavDropdown title={commodity}>
            {data.data.map((future) => (
              <NavDropdown.Item
                key={future.name}
                onClick={handleSelect}
                value={future.name}
              >
                {future.name}
              </NavDropdown.Item>
            ))}
          </NavDropdown>
        </Nav>
        <Container>
          <Navbar.Brand className="text-info ms-auto"></Navbar.Brand>
        </Container>
      </Navbar>
      <h1>Commitment of Traders Data</h1>
      <div key={selectedCommodityData[0].name}>
        <Line
          options={{
            maintainAspectRatio: true,
            responsive: true,
            hover: { mode: "nearest", intersect: false },
            layout: {
              padding: {
                left: 100,
                right: 100,
                top: 100,
              },
            },
            plugins: {
              title: {
                display: true,
                text: selectedCommodityData[0].name,
              },
              tooltip: {
                mode: "index",
                intersect: false,
                position: "nearest",
              },
            },
          }}
          data={{
            labels: selectedCommodityData[0].dates,
            datasets: [
              {
                label: "Commercial Hedgers",
                data: selectedCommodityData[0].commercial,
                borderColor: "green",
                backgroundColor: "green",
                borderJoinStyle: "round",
                pointStyle: "line",
                pointBorderWidth: 0,
              },
              {
                label: "Small Traders",
                data: selectedCommodityData[0]["non reporting"],
                borderColor: "blue",
                backgroundColor: "blue",
                borderJoinStyle: "round",
                pointStyle: "line",
                pointBorderWidth: 0,
              },
              {
                label: "Large Traders",
                data: selectedCommodityData[0]["non commercial"],
                borderColor: "red",
                backgroundColor: "red",
                borderJoinStyle: "round",
                pointStyle: "line",
                pointBorderWidth: 0,
              },
            ],
          }}
        />
        <Line
          options={{
            maintainAspectRatio: true,
            responsive: true,
            hover: { mode: "nearest", intersect: false },
            layout: { padding: { left: 100, right: 100, bottom: 100 } },
            plugins: {
              title: {
                display: true,
                text: selectedFuturePriceData[0].name,
              },
              tooltip: {
                mode: "index",
                intersect: false,
                position: "nearest",
              },
            },
          }}
          data={{
            labels: selectedFuturePriceData[0].dates,
            datasets: [
              {
                label: "Closing Price Data",
                data: selectedFuturePriceData[0].close,
                borderColor: "blue",
                backgroundColor: "blue",
                borderJoinStyle: "round",
                pointStyle: "line",
                pointBorderWidth: 0,
              },
            ],
          }}
        />
      </div>
    </div>
  );
}

export default App;

/// <Line data={{labels: future.dates, datasets: [{label: future.name, data: future.commercial}]}}/>
