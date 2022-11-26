import {
  Accordion,
  AccordionItemHeading,
  AccordionItem,
  AccordionItemPanel,
  AccordionItemButton
} from "react-accessible-accordion";

import "./App.css";
import Search from "./components/search/search";
import CurrentWeather from "./components/current-weather/current-weather";
import Forecast from "./components/forecast/forecast";
import ForecastHours from "./components/forecast/forecastHours";
import { WEATHER_API_URL, WEATHER_API_KEY,  WEATHER_API_URL1} from "./api";
import { useState } from "react";

function App() {

  const [currentWeather, setCurrentWeather] = useState(null);
  const [forecast, setForecast] = useState(null);

  const handleOnSearchChange = (searchData) => {
    const [lat, lon] = searchData.value.split(" ");

    const currentWeatherFetch = fetch(
      `${WEATHER_API_URL}/weather?lat=${lat}&lon=${lon}&appid=${WEATHER_API_KEY}&units=metric`
    );
    const forecastFetch = fetch(
      `${WEATHER_API_URL}/forecast?lat=${lat}&lon=${lon}&appid=${WEATHER_API_KEY}&units=metric`
    );

    
    Promise.all([currentWeatherFetch, forecastFetch])
      .then(async (response) => {
        const weatherResponse = await response[0].json();
        const forecastResponse = await response[1].json();

        setCurrentWeather({ city: searchData.label, ...weatherResponse });
        setForecast({ city: searchData.label, ...forecastResponse });
      })
      .catch((err) => console.log(err));

  };

  console.log(forecast);

  return (
    <div className="container">
      <Search onSearchChange={handleOnSearchChange} />
      {currentWeather && <CurrentWeather data={currentWeather} />}
                  <Accordion allowZeroExpanded>
                    <AccordionItem >
                        <AccordionItemHeading>
                            <AccordionItemButton>
                              <div className="hours-item">
                                <label className="title"> Прогноз погоды на каждые три часа </label>
                              </div>
                            </AccordionItemButton>
                          </AccordionItemHeading>
                        <AccordionItemPanel>
                          {forecast && <ForecastHours data = {forecast}/>}

                        </AccordionItemPanel>
                    </AccordionItem>
                    <AccordionItem >
                      <AccordionItemHeading>
                        <AccordionItemButton>
                            <div className="hours-item">
                                <label className="title"> Прогноз погоды на 5 дней </label>
                            </div>
                          </AccordionItemButton>
                      </AccordionItemHeading>  
                          <AccordionItemPanel>
                          {forecast && <Forecast data = {forecast}/>} 

                        </AccordionItemPanel>
                      </AccordionItem>
                  </Accordion>
    </div>
  );
}

export default App;
