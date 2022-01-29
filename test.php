<?php
class Authorization
{
  private $permissions, $users;

  public function __construct($permissions, $users)
  {
    $this->permissions = $permissions;
    $this->users = $users;
  }

  public function listPermissions($userId) {
      foreach($this->users as $key) {
          if ($key["id"]== $userId) {
              $role = $key["roles"];
              foreach($this->permissions as $val) {
                  for ($i=0;$i <= count($role); $i++) {
                      if ($role[$i] == $val["role"] and $val["active"]==true) {
                          $res[] = $val["name"];
                        }
                    }
                }
            } 
        }
        return $res;
    }

    public function checkPermitted($permissionName, $userId){
        foreach ($this->permissions as $key){
            var_dump($permissionName);
            if ($key["name"] == $permissionName){
                var_dump($key["active"]);
            } else {
                $res = false;
            }
        }
        // return $res;
    }
}

 $permissions = [
    ["role" => "superuser", "name" => "lock user account", "active" => true],
    ["role" => "superuser", "name" => "unlock user account", "active" => true],
    ["role" => "superuser", "name" => "purchase widgets", "active" => false],
    ["role" => "charger", "name" => "view pick up locations", "active" => true],
    ["role" => "rider", "name" => "view my profile", "active" => true],
    ["role" => "rider", "name" => "scooters near me", "active" => true],
  ];
  $users = [
    ["id" => 1, "name" => "Anna Administrator", "roles" => ["superuser"]],
    ["id" => 2, "name" => "Charles N. Charge", "roles" => ["charger", "rider"]],
    ["id" => 7, "name" => "Ryder", "roles" => ["rider"]],
    ["id" => 11, "name" => "Unregistered Ulysses", "roles" => []],
    ["id" => 18, "name" => "Tessa Tester", "roles" => ["beta tester"]],
  ];
$test = new Authorization($permissions,$users);
//var_dump($test->listPermissions('7'));
//var_dump($test->checkPermitted("lock user account",1));
//var_dump($test->checkPermitted("scooters near me",1));
var_dump($test->checkPermitted("purchase widgets",1));
//var_dump($test->checkPermitted("view pick up locations", 2));

?>