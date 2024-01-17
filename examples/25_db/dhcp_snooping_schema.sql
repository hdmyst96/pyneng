create table if not exists switch(mac text not NULL primary key, hostname text, model text, location text);

create table if not exists dhcp (
    mac          text not NULL primary key,
    ip           text,
    vlan         text,
    interface    text
);
