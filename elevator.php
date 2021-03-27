<?php 
class Elevator(){
    public $elevator_id;
    public $total_capacity = 10;
    public $current_capacity;
    public $current_floor;
    public $destination_floor;
    public $status; 

    public function __construct($elevator_id,$current_capacity,$status=null){
        $status = $this->status;
        $elevator_id = $this->$elevator_id;
        $current_capacity = $this->current_capacity;
        if ($current_capacity>$this->total_capacity){
            return "Overload. Reduce capacity to 10"
        }
    }
    
    public function getStatus(){
        $status = [];
        $status[] = $this->elevator_id=>$this->status;
    }

    public function chooseFloor($destination_floor){
        if ($destination_floor==$this->current_floor){
            return "Same Floor. Choose differnet floor";
        }
        else {
            $destination_floor= $this->destination_floor;
        }
    }
}

class Building(){
    public $total_floor = 10;
    
    public function getElevator(){
        foreach ($status in )
    }
}
//Add a batch function which stores the status of all instantiated elevators
//Iterated over the list of all the elevator statuses and find out the one which is free

$Elevator = new Elevator(1,5);
$Building = new Building();
var_dump($Elevator->getStatus());
?>