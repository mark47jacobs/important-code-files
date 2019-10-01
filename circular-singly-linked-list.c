/*****************************************************************************************************************************
**********************************************circular singly linked lists****************************************************
the allowed set of operations on CIRCULAR SINGLY LINKED LIST are INSERTEND() INSERTBEG() INSERTBW() DELETEEND() DELETEBEG()
                                       DELETEBW() DISPLAY() SEARCHbyVALUE()                                                     
*****************************************************************************************************************************/

#include<stdio.h>
#include<stdlib.h>

struct student
{
    int marks; struct student *link;
} *last = NULL, *temp;

void INSERTBEG()
{   
    temp = (struct student *)malloc(sizeof(struct student));
    printf("enter marks of the current student: ");
    scanf("%d",&temp->marks);
    if (last == NULL)
    {
        last = temp;
        last->link = temp; 
    }
    else
    {
        temp->link = last->link;
        last->link = temp;
    }
}

void INSERTEND()
{
    temp = (struct student *)malloc(sizeof(struct student));
    printf("enter marks of the current student: ");
    scanf("%d",&temp->marks);
    if (last == NULL)
    {
        last = temp;
        last->link = temp; 
    }
    else
    {
        temp->link = last->link;
        last->link = temp;
        last = temp;
    }
}

void INSERTBW()
{   int pos,counter = 0;
    temp = (struct student *)malloc(sizeof(struct student));
    printf("enter the position at which you want to insert: ");
    scanf("%d",&pos);
    printf("enter the marks of the current student: ");
    scanf("%d",&temp->marks);
    
    if (last == NULL)
    {
        last = temp;
        last->link = temp;
    }
    else
    {
        struct student *p,*cur;
        p = last->link;
        cur = last;
        
        while(counter < pos-1)
        {   cur = p;
            p = p->link;
            counter++;
        }
        temp->link = p;
        cur->link = temp;
    }
}

void DELETEBEG()
{
    if(last == NULL)
    {
        printf("\n the list is empty :(");
    }
    else
    {
        temp = last->link;
        last->link  = temp->link;
        free(temp);
    }
}

void DELETEBW()
{
    int pos,counter = 0;
    if(last == NULL)
    {
        printf("\n the list is empty :(");
    }
    else
    {
        printf("\n Enter the position at which you want to delete");
        scanf("%d",&pos);
        
        struct student *p,*cur;
        p = last->link;
        cur = last;
        
        while(counter <= pos)
        {   cur = p;
            p = p->link;
            counter++;
        }
        cur->link = p->link;
        free(p);
    }
}

void DELETEEND()
{
    if(last == NULL)
    {
        printf("\n the list is empty :(");
    }
    else
    {
        struct student *ptr = last->link,*cur;
        while(ptr->link!=last)
        {   cur = ptr;
            ptr = ptr->link;
        }
        ptr->link = last->link;
        last = ptr;
    }
}

void DISPLAY()
{
    struct student *temp;

    if(last == NULL)
        printf("empty\n");
    else
    {
        temp = last->link;
        while(temp != last)
        {
            printf("%d-->",temp->marks);
            temp = temp->link;
        }
        printf("%d-->", temp->marks);
        printf("\n");
    }
}

void SEARCHbyVALUE()
{
    
}

void main()
{
    int ch;
    while(1)
    {
        printf("1.insert at end\n2.display\n3.insertbeg\n4.insertmid\n5.deleteend\n6.exit\n");
        printf("enter the choice\n");
        scanf("%d", &ch);

        switch(ch)
        {
            case 1 : INSERTEND();
                     break;
            case 2 : DISPLAY();
                     break;
            case 3 : INSERTBEG();
                     break;
            case 4 : INSERTBW();
                     break;
            
            case 6 : exit(0);
                     break;
        }
    } 
}
