from app.predictor import predict_score

def main() -> None:
    study_hours = float(input("Study hours:"))
    sleep_hours = float(input("Sleep hours:"))
    
    try:
        score = predict_score(
            study_hours=study_hours,
            sleep_hours=sleep_hours,
        )
    except ValueError as error:
        print(f"Error: {error}")
        return 
    print(f"Predicted score: {score:.2f}")

if __name__ == "__main__":
    main()