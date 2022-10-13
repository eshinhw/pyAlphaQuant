import { useEffect, useState } from "react";
import { Container, Row } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import SymbolCard from "./Cards";
import BasicExample from "./Cards";
import axios from "axios";

function SymbolInput() {
  const [symbol, setSymbol] = useState("");
  const [data, setData] = useState([]);

  // useEffect(() => {
  //   console.log("Data useEffect");
  //   console.log(data);
  // });

  const onChangeInput = (e) => {
    setSymbol(e.currentTarget.value);
  };

  const onClickButton = () => {
    let newData = { symbol: symbol, description: `This is a stock ${symbol}` };
    setData([...data, newData]);
    setSymbol("");
    axios.get()
  };

  return (
    <>
      <InputGroup className="mb-3">
        <Form.Control placeholder="Type Stock Symbol" onChange={onChangeInput} value={symbol} />
        <Button variant="outline-secondary" id="button-addon2" onClick={onClickButton}>
          Add
        </Button>
      </InputGroup>
      <Container>
        <Row>
          {data.map((d, idx) => {
            console.log(d);
            return <SymbolCard key={idx} symbol={d.symbol} description={d.description} />;
          })}
        </Row>
      </Container>
    </>
  );
}

export default SymbolInput;
