import './Reviews.css';

const Review = ({ movieName, stars }) => {
  return (
    <div className='reviewsContainer'>
      <div className='reviewsUserHeader'>
        {movieName ? <p>{movieName}</p> : <p>Username</p>}
        <p>{stars} Stars</p>
      </div>
      <div className='reviewsContent'>
        Lorem Ipsum is simply dummy text of the printing and typesetting
        industry. Lorem Ipsum has been the industry's standard dummy text ever
        since the 1500s, when an unknown printer took a galley of type and
        scrambled it to make a type specimen book. It has survived not
      </div>
    </div>
  );
};
export default Review;
