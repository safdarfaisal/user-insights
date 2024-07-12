import './Reviews.css';

const Review = ({ movieName, stars=0, review='', userName='' }) => {
  return (
    <div className='reviewsContainer'>
      <div className='reviewsUserHeader'>
        {movieName ? <p>{movieName} : {userName} </p> : <p> </p>}
        <p>{stars} Stars</p>
      </div>
      <div className='reviewsContent'>
        {review}
      </div>
    </div>
  );
};
export default Review;
