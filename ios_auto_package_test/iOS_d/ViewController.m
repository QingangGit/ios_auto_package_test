//
//  ViewController.m
//  iOS_d
//
//  Created by qin on 2020/1/8.
//  Copyright © 2020年 Mplanet. All rights reserved.
//

#import "ViewController.h"
#import "QLlabel.h"
#import "QLlabel+categ.h"

#import "qllLabel.h"
#import "Qstr.h"
#import "Qstr+cate.h"
#import "qSte_sub.h"
#import "QLlabel+extension.h"
@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib
//category
    NSLog(@"%s",object_getClassName(self));

    QLlabel *lb = [[QLlabel alloc] init];
    lb.t_s = @"QLlabel";
    NSLog(@"%@",lb.t_s);

    [lb cate_show];
    [lb category_test];


    lb.QLlabel_str = @"QLlabel_str_set";

    NSLog(@"======================================================================");

    qllLabel *ql= [[qllLabel alloc] init];
    ql.t_s = @"qllLabel";
    NSLog(@"%@",ql.t_s);
    [ql cate_show];
    [ql qllLabel_show];
    
    [[qSte_sub new] qStrlog];
    
//extension
    
}


@end
