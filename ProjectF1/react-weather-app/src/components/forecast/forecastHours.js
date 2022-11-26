import {
    Accordion,
    AccordionItemHeading,
    AccordionItem,
    AccordionItemPanel,
    AccordionItemButton
} from "react-accessible-accordion";
import './forecast.css';

// const WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

const ForecastHours = ({ data }) => {

    const dataWeather = data.list.slice(0,10)

    return (
        <>
        
            <label className="title">Почасовой прогноз </label>
            <Accordion allowZeroExpanded>
                {dataWeather.map((item, idx) => (
                    <AccordionItem key={idx}>
                        <AccordionItemHeading>
                            <AccordionItemButton>
                                <div className="daily-item">
                                    <img
                                        alt="weather"
                                        className="icon-small"
                                        src={`icons/${item.weather[0].icon}.png`}
                                    />
                                    <label className="day">{item.dt_txt}</label>
                                    <label className="description">{item.weather[0].description}</label>
                                    <label className="min-max">
                                        {Math.round(item.main.temp_min)}°C /
                                        {Math.round(item.main.temp_max)}°C
                                    </label>
                                </div>
                            </AccordionItemButton>
                        </AccordionItemHeading>
                        <AccordionItemPanel>
                        <div className="daily-details-grid">
                                <div className="daily-details-grid-item">
                                    <label>Давление:</label>
                                    <label>{item.main.pressure} hPa</label>
                                </div>
                                <div className="daily-details-grid-item">
                                    <label>Влажность:</label>
                                    <label>{item.main.humidity}%</label>
                                </div>
                                <div className="daily-details-grid-item">
                                    <label>Облачность:</label>
                                    <label>{item.clouds.all}%</label>
                                </div>
                                <div className="daily-details-grid-item">
                                    <label>Скорость ветра:</label>
                                    <label>{item.wind.speed} m/s</label>
                                </div>
                                <div className="daily-details-grid-item">
                                    <label>Высота над уровнем моря:</label>
                                    <label>{item.main.sea_level}</label>
                                </div>
                                <div className="daily-details-grid-item">
                                    <label>Ощущается как:</label>
                                    <label>{Math.round(item.main.feels_like)}°C</label>
                                </div>
                            </div>
                        </AccordionItemPanel>
                    </AccordionItem>

                ))}
            </Accordion>
        </>
    );
};

export default ForecastHours; 